def palindromes_of_specific_lengths(str_):
    str_ = str_.lower()
    ret = set()
    for i in range(15, 96):
        for j in range(i - 19, i + 1):
            if j < 0 or len(str_) <= j:
                continue
            if str_[j] not in string.ascii_letters:
                continue
            is_palin = True
            for k in range((i - j) // 2):
                if str_[j + k] != str_[j + (i - j) - 1 - k]:
                    is_palin = False
                    break
            if is_palin:
                ret.add(str_[j:i + 1])
    return ret