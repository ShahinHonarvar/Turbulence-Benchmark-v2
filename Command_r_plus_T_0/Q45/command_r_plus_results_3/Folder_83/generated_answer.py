def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[2:10])
    palindromes = set()
    for letter in english_letters:
        if letter in s_letters:
            start_index = s.find(letter, 2, 10)
            end_index = s.rfind(letter, 2, 10)
            if start_index != -1 and end_index != -1 and (abs(start_index - end_index) >= 6):
                palindrome = s[start_index:end_index + 1]
                if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes