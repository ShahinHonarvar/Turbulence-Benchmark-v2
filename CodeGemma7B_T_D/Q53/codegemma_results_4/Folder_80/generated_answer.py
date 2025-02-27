def palindrome_of_length_at_least_n(text):
    text = text.lower()
    for i in range(len(text) - 29):
        first = text[i]
        second = text[i + 1]
        third = text[i + 2]
        palindrome = first + second + third
        if palindrome.isalpha():
            Palindromes.add(palindrome)
        for j in range(i + 3, len(text)):
            next_letter = text[j]
            palindrome = palindrome + next_letter
            if palindrome.isalpha():
                Palindromes.add(palindrome)
            if len(palindrome) >= 30:
                return Palindromes
    return set()