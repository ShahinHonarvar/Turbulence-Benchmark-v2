def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindrome_set = set()
    for i in range(12, 93):
        for length in range(42, 78):
            if i + length <= 92:
                substring = input_string[i:i + length]
                if substring.lower().count(substring[0].lower()) == len(substring) and set(substring).issubset(english_letters):
                    if substring.lower() == substring.lower()[::-1]:
                        palindrome_set.add(substring.lower())
    return palindrome_set