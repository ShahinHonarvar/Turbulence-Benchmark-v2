def palindromes_of_specific_lengths(input_string):
    substring = input_string[23:83]
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            snippet = substring[i:i + length]
            if snippet.lower() == snippet.lower()[::-1]:
                english_palindrome = ''.join(filter(str.isalpha, snippet.lower()))
                if len(english_palindrome) in [32, 33, 34] and english_palindrome == english_palindrome[::-1]:
                    palindromes.add(english_palindrome)
    return palindromes