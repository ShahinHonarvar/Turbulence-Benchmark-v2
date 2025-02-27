def palindromes_of_specific_lengths(word):
    set_palindromes = set()
    for i in range(29, 97):
        str1 = word[i:i + 12]
        str2 = word[i:i + 18]
        if is_palindrome(str1) or is_palindrome(str2):
            set_palindromes.add(str1.lower() if is_palindrome(str1) else str2.lower())
    return set_palindromes