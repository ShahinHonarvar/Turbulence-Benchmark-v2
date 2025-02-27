def palindromes_between_indices(string):
    start_index = 3
    end_index = 5
    palindromes = set()
    letters = {}
    for char in string:
        if char.isalpha():
            letters[char.lower()] = letters.get(char.lower(), 0) + 1
    for permutation in itertools.permutations(letters.keys()):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3 and palindrome[start_index:end_index + 1] == palindrome[end_index:start_index:-1]:
            palindromes.add(palindrome)
    return palindromes