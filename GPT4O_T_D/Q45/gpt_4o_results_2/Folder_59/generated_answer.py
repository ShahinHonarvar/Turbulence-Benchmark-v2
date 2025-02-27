def palindromes_between_indices(s):

    def is_palindrome(letters):
        return letters == letters[::-1]
    if len(s) < 10:
        return set()
    substring = s[8:10].lower()
    letters = [char for char in substring if char.isalpha()]

    def possible_palindromes(letters):
        if len(letters) < 3:
            return set()
        possible = set()
        length = len(letters)
        if length % 2 == 0:
            mid = length // 2
        else:
            mid = length // 2 + 1
        for i in range(mid + 1):
            for j in range(i, length):
                temp = ''.join(letters[i:j + 1])
                if len(temp) > 2 and is_palindrome(temp):
                    possible.add(temp)
        return possible
    return possible_palindromes(letters)