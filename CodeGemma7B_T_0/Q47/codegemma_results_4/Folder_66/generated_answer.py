from index 32 to index 79, both inclusive. The function is case-insensitive.

def palindromes_of_specific_lengths(text):
    """
    This function takes a string as input and returns a set of all palindromes
    of lengths between 35 and 41 (inclusive) that occur in the substring
    """
    text = text.lower()
    palindromes = set()
    for i in range(32, 80):
        for j in range(i + 35, i + 42):
            if j - i + 1 == j - i:
                palindrome = text[i:j + 1]
                if palindrome in palindromes:
                    continue
                palindromes.add(palindrome)
    return palindromes