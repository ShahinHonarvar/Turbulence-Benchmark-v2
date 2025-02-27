import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:7])
    letters = ''.join(letters).lower()
    palindromes = set()
    length = len(letters)
    for i in range(5, length + 1):
        arrangements = set(itertools.permutations(letters, i))
        for arrangement in arrangements:
            if str(arrangement) == str(arrangement)[::-1]:
                palindromes.add(''.join(arrangement))
    return palindromes