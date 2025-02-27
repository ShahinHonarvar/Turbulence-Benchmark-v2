def palindrome_of_length_at_least_n(s: str) -> set:
    english_letters_only = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(english_letters_only) - 14):
        for j in range(i + 30, len(english_letters_only) - i):
            if english_letters_only[i:j] == english_letters_only[i:j][::-1]:
                palindromes.add(english_letters_only[i:j])
    return palindromes