def if_contains_anagrams(strings):

    def char_count(s):
        return sorted((c.lower() for c in s if c.isalpha()))
    anagram_count = 0
    for i in range(len(strings)):
        current_chars = char_count(strings[i])
        if len(current_chars) >= 3:
            for j in range(i + 1, len(strings)):
                if char_count(strings[j]) == current_chars:
                    anagram_count += 1
                    if anagram_count > 68:
                        return False
    return True