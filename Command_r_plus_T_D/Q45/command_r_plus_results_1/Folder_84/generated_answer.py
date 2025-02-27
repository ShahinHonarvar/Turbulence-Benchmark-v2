import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[4:10])
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for combo in combinations(letters, i):
            if combo[0::2] == combo[1::2][::-1]:
                palindromes.add(''.join(combo))
    return palindromes