from collections import defaultdict

def palindromes_between_indices(s):
    result = set()
    english_letters = {chr(i).upper(): 0 for i in range(ord('A'), ord('Z') + 1)}
    for i in range(1, 4):
        for j in range(i, 4):
            letters = defaultdict(int, **english_letters)
            for k in range(i, j + 1):
                letters[s[k]] += 1
            if any((count % 2 != 0 for count in letters.values())):
                continue
            palindrome = ''.join((key * (val // 2) for key, val in letters.items()))
            result.add(palindrome)
    return result