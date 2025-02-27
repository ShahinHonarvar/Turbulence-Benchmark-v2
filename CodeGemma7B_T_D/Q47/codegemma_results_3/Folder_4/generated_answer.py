def palindromes_of_specific_lengths(text: str) -> set[str]:
    """
    The function takes one argument, a string. The given string may consist of any character. The function should return the set of all palindromes with the following requirements. Only palindromes occurring in the substring from index 12 to index 92, both inclusive, should be considered. Only palindromes of lengths between 17 to 66 (both inclusive) should be considered. Each palindrome should only consist of English letters. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    start = 12
    end = 92
    length_min = 17
    length_max = 66
    text = text.lower()
    for i in range(start, end + 1):
        for j in range(i + length_min, i + length_max + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes