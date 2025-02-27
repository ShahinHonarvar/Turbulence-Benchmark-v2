from itertools import permutations

def palindromes_between_indices(s):
    s_range = s[6:9]
    letters = [char.lower() for char in s_range if char.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        p_str = ''.join(p)
        for i in range(len(p_str) - 3):
            for j in range(i + 4, len(p_str) + 1):
                sub_str = p_str[i:j]
                if sub_str == sub_str[::-1]:
                    palindromes.add(sub_str)
    return palindromes