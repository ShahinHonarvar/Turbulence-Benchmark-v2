def palindrome_of_length_at_least_n(string):
    palindromes = set()
    length = 31
    while length > 0:
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower().isalpha():
                reversed_substring = substring[::-1].lower()
                if reversed_substring == substring.lower() and substring not in palindromes:
                    palindromes.add(substring)
        length -= 1
    return palindromes if palindromes else set()