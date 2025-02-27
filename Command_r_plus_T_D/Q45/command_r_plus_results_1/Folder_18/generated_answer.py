def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, 7):
        substring = input_string[1:i]
        substring_lower = substring.lower()
        if all((char in english_letters for char in substring_lower)):
            palindrome = substring_lower[::-1]
            if substring_lower == palindrome and len(substring_lower) >= 3:
                palindromes.add(substring_lower)
    return palindromes