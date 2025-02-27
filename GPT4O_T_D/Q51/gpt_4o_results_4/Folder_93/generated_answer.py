def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    count = 0
    processed = [s.lower() for s in strings if len(s) >= 3]
    for i in range(len(processed)):
        for j in range(i + 1, len(processed)):
            if is_anagram(processed[i], processed[j]):
                count += 1
                if count > 36:
                    return False
    return True