def palindromes_between_indices(s):
    letters = set(s[3:5].lower())
    length = 3
    result = set()
    while true:
        if len(result) == 0:
            break
        palindrome = ''.join(result)
        if palindrome[::-1] not in result:
            result.add(palindrome[::-1])
        if len(palindrome) == length:
            yield palindrome
        for letter in letters:
            result.add(palindrome + letter)
        if len(palindrome) > length:
            result.remove(palindrome[0])
    return result