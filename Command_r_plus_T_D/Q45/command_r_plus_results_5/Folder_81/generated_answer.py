def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_lower = s[:7].lower()
    s_lower_set = set(s_lower)
    palindromes = set()
    for letter in s_lower:
        if letter in english_letters:
            s_lower_set.remove(letter)
            break
    for letter in reversed(s_lower):
        if letter in english_letters:
            s_lower_set.remove(letter)
            break
    for letter in s_lower_set:
        if s_lower.count(letter) >= 2:
            s_lower_set.remove(letter)
    for letter in s_lower_set:
        palindrome = s_lower[:3] + letter + s_lower[-3:]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes