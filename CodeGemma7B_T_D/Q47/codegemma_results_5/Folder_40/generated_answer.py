def palindromes_of_specific_lengths(str):
    """
    Returns a set of all palindromes in the substring from index 0 to index 5, inclusive.
    Only palindromes of lengths between 3 to 5 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    """
    result = set()
    for i in range(len(str)):
        for j in range(i + 3, min(i + 6, len(str))):
            palindrome = str[i:j + 1]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result