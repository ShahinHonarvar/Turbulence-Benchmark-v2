def palindromes_between_indices(string):
    letters = [char.lower() for char in string[3:7]]
    return {''.join(palindrome) for size in range(3, len(letters) + 1) for palindrome in itertools.permutations(letters, size) if palindrome == palindrome[::-1]}