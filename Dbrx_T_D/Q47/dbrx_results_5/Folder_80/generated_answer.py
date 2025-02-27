def palindromes_of_specific_lengths(value):

    def is_palindrome(pal):
        return pal.lower() == pal.lower()[::-1]
    result = set()
    for i in range(35, 89):
        for j in range(24, 34):
            if i + j - 1 <= 88 and is_palindrome(value[i:i + j]):
                result.add(value[i:i + j])
    return result