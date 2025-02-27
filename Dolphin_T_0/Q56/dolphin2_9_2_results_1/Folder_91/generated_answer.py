def all_substring_of_size_n(s):

    def isUnique(s):
        chars = set()
        for char in s:
            if char in chars:
                return False
            chars.add(char)
        return True
    n = 6
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    return [s for s in substrings if isUnique(s)]