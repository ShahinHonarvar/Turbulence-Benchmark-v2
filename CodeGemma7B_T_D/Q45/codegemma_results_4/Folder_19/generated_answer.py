def palindromes_between_indices(string):
    string = string.lower()
    substring = string[1:8]
    if not substring.isalpha():
        return set()
    arrangements = itertools.permutations(substring)
    palindromes = set()
    for arrangement in arrangements:
        palindrome = ''.join(arrangement)
        palindromes.add(palindrome)
    valid_palindromes = {palindrome for palindrome in palindromes if len(palindrome) >= 7}
    return valid_palindromes or set()