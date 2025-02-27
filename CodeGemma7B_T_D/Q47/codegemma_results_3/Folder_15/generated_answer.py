def palindromes_of_specific_lengths(input_str):
    """Given string may consist of any character.
       Return the set of all palindromes with the following requirements.
       Only palindromes occurring in the substring from index 0 to index 6, both inclusive, should be considered.
       Only palindromes of lengths between 3 to 6 (both inclusive) should be considered.
       Each palindrome should only consist of English letters.
       If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
       The function should find the palindromes in a case-insensitive manner."""
    palindrome_set = set()
    for ss in range(len(input_str) - 6 + 1):
        s = input_str[ss:ss + 7]
        for len in range(3, 7):
            for ss in range(len):
                if s[ss] >= 'a' and s[ss] <= 'z' and (s[-ss - 1] >= 'a') and (s[-ss - 1] <= 'z') and (s[ss] == s[-ss - 1]):
                    palindrome_set.add(s)
    return palindrome_set