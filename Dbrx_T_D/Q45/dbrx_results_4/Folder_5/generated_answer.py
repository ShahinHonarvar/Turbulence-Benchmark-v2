from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')

    def valid_palindrome(arr):
        if len(arr) < 4:
            return False
        first_half, second_half = (arr[:len(arr) // 2], arr[len(arr) // 2:][::-1])
        return first_half == second_half and all((x.lower() in eng_letters for x in first_half))
    return {s[i:j + 1]: None for i in range(4, 8 + 1) for j in range(i, 8 + 1) if valid_palindrome(list(s[i:j + 1]))}.keys()