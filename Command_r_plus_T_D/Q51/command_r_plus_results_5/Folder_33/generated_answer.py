def if_contains_anagrams(lst):

    def normalize_text(text):
        return text.lower()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                normalized_i = normalize_text(lst[i])
                normalized_j = normalize_text(lst[j])
                if is_anagram(normalized_i, normalized_j):
                    anagram_count += 1
                    if anagram_count > 85:
                        return False
    return True