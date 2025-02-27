def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    relevant_letters = [char.lower() for char in s[4:7] if char.lower() in english_letters]
    for i in range(4, len(relevant_letters) + 1):
        for j in range(len(relevant_letters) - i + 1):
            palindrome = ''.join(relevant_letters[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes