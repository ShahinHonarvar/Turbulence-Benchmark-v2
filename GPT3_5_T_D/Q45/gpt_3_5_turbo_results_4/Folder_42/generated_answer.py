import itertools
    import string

def palindromes_between_indices(s):
    substring = s[6:10]
    english_letters = set(string.ascii_letters)
    filtered_substring = ''.join(filter(lambda x: x in english_letters, substring))
    arrangements = set((''.join(perm) for perm in itertools.permutations(filtered_substring)))
    palindromes = set()
    for word in arrangements:
        if len(word) >= 3 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes