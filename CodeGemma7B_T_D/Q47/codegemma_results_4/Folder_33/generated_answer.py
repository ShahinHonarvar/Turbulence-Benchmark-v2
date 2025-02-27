def palindromes_of_specific_lengths(txt):
    letters_only = ''.join((char for char in txt[130:295].lower() if char.isalpha()))
    all_palindromes = set()
    for length in range(103, 159):
        for start in range(len(letters_only) - length + 1):
            palindrome = letters_only[start:start + length]
            if palindrome == palindrome[::-1]:
                all_palindromes.add(palindrome)
    return all_palindromes