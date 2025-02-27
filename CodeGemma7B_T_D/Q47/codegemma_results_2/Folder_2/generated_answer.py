def palindromes_of_specific_lengths(str):
    """Sorts a list of integers in ascending order."""
    result = set()
    for i in range(40, 101):
        for j in range(i):
            substring = str[i - j - 1:i + j + 1]
            if substring.lower() == substring.lower()[::-1] and len(substring) >= 18 and (len(substring) <= 36):
                result.add(substring)
    return result