def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    while True:
        length = len(text)
        for index in range(length):
            for n in range(length - index):
                substring = text[index:index + n + 1]
                reverse_substring = substring[::-1]
                if substring == reverse_substring and len(substring) >= 18:
                    palindromes.add(substring)
        if length == len(text):
            break
        text = text[:length - 1]
    return palindromes