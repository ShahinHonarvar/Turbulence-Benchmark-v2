from collections import defaultdict

def palindromes_between_indices(s):
    result = set()
    for i in range(2, 8):
        for j in range(i, 8):
            chars = s[2:8][i:j + 1]
            if len(chars) >= 6:
                chars = chars.lower()
                chars_dict = defaultdict(int)
                for char in chars:
                    chars_dict[char] += 1
                if len(chars_dict) == 26:
                    result.add(''.join(sorted(chars_dict.keys())))
    return result