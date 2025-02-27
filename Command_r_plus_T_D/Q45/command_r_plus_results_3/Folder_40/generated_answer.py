def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = {char.lower() for char in s[4:10] if char.lower() in english_letters}
    for palindrome_length in range(7, len(letters_in_range) + 1):
        if palindrome_length % 2 == 0:
            for i in range(len(letters_in_range) - palindrome_length + 1 + 1):
                first_half = ''.join(letters_in_range)[:palindrome_length // 2]
                second_half = ''.join(reversed(first_half))
                palindromes.add(first_half + second_half)
        else:
            for i in range(len(letters_in_range) - palindrome_length + 1):
                first_half = ''.join(letters_in_range)[:palindrome_length // 2]
                second_half = ''.join(reversed(first_half))
                palindromes.add(first_half + s[9] + second_half)
    return palindromes