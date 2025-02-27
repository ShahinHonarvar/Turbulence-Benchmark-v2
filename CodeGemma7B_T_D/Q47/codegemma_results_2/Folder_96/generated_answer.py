def palindromes_of_specific_lengths(txt):
    """
    Write a function called 'palindromes_of_specific_lengths' that takes one argument, a string.
    The given string may consist of any character.
    The function should return the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 100 to index 300, both inclusive, should be considered.
    Only palindromes of lengths between 50 to 100 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    case_insensitive_txt = txt.lower()
    palindromes = set()
    for i in range(100, 301):
        for j in range(i - 49, i + 1):
            if j >= 0 and j < len(case_insensitive_txt):
                palindrome = case_insensitive_txt[j:i + 1]
                if palindrome == palindrome[::-1] and len(palindrome) >= 50 and (len(palindrome) <= 100):
                    palindromes.add(palindrome)
    return palindromes