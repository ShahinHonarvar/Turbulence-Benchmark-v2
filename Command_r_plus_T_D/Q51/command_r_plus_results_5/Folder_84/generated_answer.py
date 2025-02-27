def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sorted_text(text: str) -> str:
        return ''.join(sorted(text))
    normalized_lst = [normalize_text(word) for word in lst]
    sorted_lst = [sorted_text(word) for word in normalized_lst]
    anagram_count = 0
    for i in range(len(sorted_lst)):
        for j in range(i + 1, len(sorted_lst)):
            if sorted_lst[i] == sorted_lst[j] and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                anagram_count += 1
                if anagram_count > 16:
                    return False
    return True