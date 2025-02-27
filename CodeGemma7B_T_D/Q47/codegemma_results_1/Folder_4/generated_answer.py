def palindromes_of_specific_lengths(text):
    text = text.lower()
    set_palindrome = set()
    for i in range(12, 92 + 1):
        for j in range(17, 66 + 1):
            palindrome = text[i - j:i]
            if palindrome == palindrome[::-1]:
                set_palindrome.add(palindrome)
    return set_palindrome