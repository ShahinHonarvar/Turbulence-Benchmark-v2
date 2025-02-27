from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(counter):
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(counter):
        palindromes = set()
        letters = [char for char in counter if counter[char] % 2 != 0]
        half = {char: counter[char] // 2 for char in counter}

        def backtrack(path, left, right):
            if len(path) >= 7:
                palindrome = path + letters[0] + path[::-1] if letters else path + path[::-1]
                palindromes.add(palindrome)
            if left > 0:
                for char in half:
                    if half[char] > 0:
                        half[char] -= 1
                        backtrack(path + char, left - 1, right)
                        half[char] += 1
        backtrack('', sum(half.values()), sum(half.values()))
        return palindromes
    counter = Counter((char.lower() for char in s[2:10] if char.isalpha()))
    if is_palindrome(counter):
        return generate_palindromes(counter)
    return set()