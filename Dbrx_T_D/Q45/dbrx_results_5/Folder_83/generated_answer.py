import re
    from collections import defaultdict

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:10])
    palindrome_dict = defaultdict(set)
    for i in range(1, len(letters) - 1):
        for j in range(i + 1, len(letters) + 1):
            sub = letters[i - 1:j]
            if sub == sub[::-1]:
                palindrome_dict[-len(sub), tuple(sub)].add(''.join(sub))
    palindromes = set()
    for _, v in palindrome_dict.items():
        palindromes.update(v)
    return {p.lower() for p in palindromes}