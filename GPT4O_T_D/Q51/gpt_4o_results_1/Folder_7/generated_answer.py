def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    processed_strings = [sorted_string(s) for s in strings if len(s) >= 3]
    for i in range(len(processed_strings)):
        for j in range(i + 1, len(processed_strings)):
            if processed_strings[i] == processed_strings[j]:
                anagram_count += 1
                if anagram_count > 445:
                    return False
    return True