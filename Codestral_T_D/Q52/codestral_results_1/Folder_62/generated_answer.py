def palindrome_of_length_n(strng):
    n = 188
    length = len(strng)
    palindromes = set()
    for i in range(length - n + 1):
        substring = strng[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes