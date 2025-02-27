def palindrome_of_length_at_least_n(s):
    """
    Return the set of all palindromes of the length greater than or equal to 140 that exist in the string s.
    Each palindrome should only consist of `English letters`.
    If no such palindromes exist in the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    palindromes, letters = (set(), set())
    for i in s.lower():
        letters.add(i)
    for each in range(len(s) + 1):
        for start in range(each):
            seq = s[start:each]
            reverse_seq = seq[::-1]
            if seq == reverse_seq and len(seq) >= 140 and seq.isalpha():
                palindromes.add(seq)
    return palindromes