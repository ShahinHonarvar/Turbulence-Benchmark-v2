from Q46.gemini_1_5_pro_results_2.Folder_86.generated_answer import gcf_three_nums
import random

# The largest index parameter based on which to generate lists.
largest_index = max(int(341), int(238), int(374))


def test_list_of_ones():
    list_of_ones = [1 for i in range(0, (largest_index + 1) * 2)]
    assert gcf_three_nums(list_of_ones) == 1


def test_list_of_same_number():
    for n in range(2, 21):
        list_of_same_nums = [n for i in range(0, (largest_index + 1) * 2)]
        assert gcf_three_nums(list_of_same_nums) == n


def test_list_of_prime_numbers():
    primes_list = [2, 3, 5, 7, 11] * (largest_index + 1)
    if primes_list[341] == primes_list[238] and primes_list[238] == primes_list[374]:
        assert gcf_three_nums(primes_list) == primes_list[341]
    else:
        assert gcf_three_nums(primes_list) == 1


# To control the testing cost, only if the largest index does not exceed 10, this test will run.
def test_power_of_num():
    if largest_index <= 10:
        for n in [2, 3]:
            power_list = [pow(n,i) for i in range(1, largest_index + 4)]
            expected_result = min(power_list[341], power_list[238], power_list[374])
            assert gcf_three_nums(power_list) == expected_result


def test_result_is_divisible_by_numbers():
    list_of_nums = random.choices(range(1,3000), k=(largest_index + 1) * 2)
    result = gcf_three_nums(list_of_nums)
    assert list_of_nums[341] % result == 0 and list_of_nums[238] % result == 0 and list_of_nums[374] % result == 0


def test_sum_of_nums():
    list_of_nums = random.choices(range(1,3000), k=(largest_index + 1) * 2)
    result = gcf_three_nums(list_of_nums)
    assert (list_of_nums[341] + list_of_nums[238] + list_of_nums[374]) % result == 0


def test_multiplication_of_nums():
    list_of_nums = random.choices(range(1,3000), k=(largest_index + 1) * 2)
    result = gcf_three_nums(list_of_nums)
    assert (list_of_nums[341] * list_of_nums[238] * list_of_nums[374]) % result == 0