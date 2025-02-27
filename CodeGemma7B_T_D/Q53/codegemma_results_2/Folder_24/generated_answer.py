def palindrome_of_length_at_least_n(string):
    """Returns the set of all palindromes of the length greater than or equal to n that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner."""
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j + 1] == string[j:i:-1]:
                if len(string[i:j + 1]) >= 53:
                    palindromes.add(string[i:j + 1])
    return palindromes