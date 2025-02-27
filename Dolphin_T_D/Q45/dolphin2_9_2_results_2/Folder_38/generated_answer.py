def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    return {i for i in set(letters) if i == i[::-1] and len(i) >= 5}