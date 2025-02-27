def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    english_letters.update('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_between_indices = {char for char in s[2:9] if char in english_letters}
    for palindrome_length in range(7, len(letters_between_indices) + 1):
        if palindrome_length % 2 == 0:
            for i in range(len(letters_between_indices) - palindrome_length + 1):
                potential_palindrome = ''.join(letters_between_indices[i:i + palindrome_length])
                if potential_palindrome == potential_palindrome[::-1]:
                    palindromes.add(potential_palindrome)
        else:
            for i in range(len(letters_between_indices) - palindrome_length + 1):
                potential_palindrome = ''.join(letters_between_indices[i:i + palindrome_length])
                if potential_palindrome == potential_palindrome[::-1]:
                    palindromes.add(potential_palindrome)
    return palindromes