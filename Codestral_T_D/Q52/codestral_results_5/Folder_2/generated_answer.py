def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length - 146):
        substring = string[i:i + 147]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes