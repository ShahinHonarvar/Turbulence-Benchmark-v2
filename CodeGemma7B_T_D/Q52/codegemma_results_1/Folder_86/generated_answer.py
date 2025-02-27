def palindrome_of_length_n(str):
    """
    palindromes of a given length 
    """
    palindrome = set()
    for i in range(len(str)):
        for n in range(i + 1, len(str)):
            substring = str[i:n]
            substring = substring.lower()
            substring = substring[::-1]
            if substring == substring:
                palindrome.add(substring)
    return palindrome