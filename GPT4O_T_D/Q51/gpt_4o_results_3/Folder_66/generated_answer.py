def if_contains_anagrams(strings):

    def processed(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    processed_strings = [processed(s) for s in strings if len(s) >= 3]
    for i in range(len(processed_strings)):
        for j in range(i + 1, len(processed_strings)):
            if processed_strings[i] == processed_strings[j]:
                anagram_count += 1
                if anagram_count > 64:
                    return False
    return True