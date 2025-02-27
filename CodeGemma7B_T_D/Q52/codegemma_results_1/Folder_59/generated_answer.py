def palindrome_of_length_n(substring):
    """
    A function that takes one argument, a string, and returns the set of all palindromes of the length equal to specified 'n', where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    substring = substring.lower()
    length = 39
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, min(i + length + 1, len(substring) + 1)):
            substring_slice = substring[i:j]
            substring_slice_reversed = substring_slice[::-1]
            if substring_slice == substring_slice_reversed:
                palindromes.add(substring_slice)
    if not palindromes:
        return set()
    return palindromes