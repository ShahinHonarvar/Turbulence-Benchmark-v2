from collections import defaultdict, deque

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def find_palindromes_util(s, start, end, palindromes):
        if start > end:
            return
        for i in range(start, end + 1):
            for j in range(i, end + 1):
                substring = s[i:j + 1]
                if is_palindrome(substring):
                    palindromes.add(substring)
        find_palindromes_util(s, start + 1, end - 1, palindromes)

    def find_palindromes(s, indices):
        if not s or not indices or (not indices[0] <= indices[1]) or (indices[1] - indices[0] < 3):
            return set()
        characters = defaultdict(int)
        for i in range(indices[0], indices[1] + 1):
            characters[s[i].lower()] += 1
        filtered_chars = [char for char in characters if characters[char] % 2 == 1]
        if len(filtered_chars) > 3:
            return set()
        half = (indices[1] - indices[0]) // 2
        for i in range(half, len(filtered_chars)):
            characters[filtered_chars[i]] += 1
        palindromes = set()
        find_palindromes_util(s, indices[0], indices[0] + half, palindromes)
        return palindromes
    return find_palindromes(s, (0, 7))