def palindromes_of_specific_lengths(s):
    """
    Returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 16 to index 94, both inclusive, should be considered.
    Only palindromes of lengths between 39 to 52 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    result = set()
    for i in range(16, 95):
        for j in range(39, 53):
            for k in range(i - j + 1):
                sub_str = s[i - j + k:i + k + 1]
                if sub_str == sub_str[::-1] and sub_str.isalpha():
                    result.add(sub_str.lower())
    return result