def all_left_truncatable_prime(x: tuple[int]) -> list[int]:
    result: list[int] = []
    for num in x:
        str_num = str(num)
        if not '0' in str_num:
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    break
            else:
                result.append(num)
    result.sort(reverse=True)
    return result

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True